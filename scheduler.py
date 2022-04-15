
from flask import Flask, render_template, request, redirect, url_for
import scheduled_jobs
import psutil
import pandas
import os
import json

app = Flask(__name__)
scheduled_jobs.scheduler.init_app(app)
scheduled_jobs.scheduler.start()

@app.route("/", methods=['POST', 'GET'])
def tasks():
    if request.method == 'POST':
        run_job = request.form.get('submit_button')
        if run_job is not None:
            try:
                job = scheduled_jobs.scheduler.get_job(run_job)
                job.func()
            except Exception as error:
                print(error)
    jobs = scheduled_jobs.scheduler.get_jobs()
    return render_template('schedule.html', jobs=jobs, title='Scheduler')


@app.route("/log")
def processes():
    file_location = scheduled_jobs.log_directory  
    def is_running(pid):
        if psutil.pid_exists(pid) and os.path.basename(psutil.Process(pid).cmdline()[0]) == 'python.exe':
            return 'running'
        else:
            return 'terminated'

    def get_data(file_name):
        log = []
        for line in open(file_name, 'r'):
            log.append(json.loads(line))
        log = pandas.json_normalize(log)
        pids = log['pid'].unique()
        pid_status = pandas.DataFrame()
        for pid in pids:
            status = is_running(pid)
            pid_result = {'pid': pid, 'status': status}
            pid_status = pid_status.append(pid_result, ignore_index=True)
        log['time'] = pandas.to_datetime(log['time']).dt.strftime('%m-%d-%Y %H:%M')
        log_data = pandas.merge(log, pid_status, on='pid')
        log_data = log_data.sort_values(by=['time'], ascending=False)
        
        return log_data
    
    processes = []

    for file in os.listdir(file_location):
        if file.endswith('.json'):
            processes.append(f'{file_location}\{file}')
    
    process_logs = {}
    process_status = {}

    for process in processes:
        id = os.path.basename(process).split('.')[0]
        log_data = get_data(process)
        process_logs[id]=log_data
        process_status[id] = {'status': log_data['status'].iloc[0], 'pid': log_data['pid'].iloc[0]}
        
    return render_template('process.html', title='Logs', sever='server', log_data=process_logs, process_status=process_status)

@app.route("/error404")
def error404():
    return render_template('error404.html')


@app.errorhandler(404)
def internal_error(error):
    return redirect(url_for('error404'))

if __name__ =='__main__':
    app.run(debug=True)