from asyncio import subprocess
from flask import Flask, render_template, request, redirect
import scheduled_jobs
import psutil
import time
import subprocess
import pandas
import os
import json

app = Flask(__name__)
scheduled_jobs.scheduler.init_app(app)
scheduled_jobs.scheduler.start()

@app.route("/scheduler")
def tasks():
    jobs = scheduled_jobs.scheduler.get_jobs()
    return render_template('blank.html', jobs=jobs)


@app.route("/processes", methods=['POST', 'GET'])
def processes():

    file_location = r'C:\Users\jwilliams\Local Files\Scripty'   
    def is_running(pid):
        if psutil.pid_exists(pid) and os.path.basename(psutil.Process(pid).cmdline()[0]) == 'python.exe':
            return 'running'
        else:
            return 'terminated'

    if request.method == 'POST':
        script = request.form.get('submit_button')
        if script is not None:
            # print('button is', script)
            if script.isdigit():
                pid = int(script)
                if is_running(pid):
                    # p = psutil.Process(pid)
                    psutil.Process(pid).terminate()
            else:
                file_path = f'{file_location}\{script}.py'
                subprocess.Popen(['python', file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
            time.sleep(1)
        return 

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
        id = os.path.basename(process).split('.')[0]#+'.py'
        log_data = get_data(process)
        # table = log_data.to_html(index=False, classes='table table-sm  collapse log', table_id=id) {{ log | safe }}
        process_logs[id]=log_data
        process_status[id] = {'status': log_data['status'].iloc[0], 'pid': log_data['pid'].iloc[0]}
        

    return render_template('process.html', title='Processes', sever='server', log_data=process_logs, process_status=process_status)


if __name__ =='__main__':
    app.run(debug=True)