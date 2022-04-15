from flask_apscheduler import APScheduler
import os

#### Add Imports here

import receptExport
import crossroadsExport
import nonfilerImport
import ascentisETL
# import partnershipImports


output_log = 'C:\logger.json'

scheduler = APScheduler()
trigger = 'Scheduler'
log_directory = r'C:\Scheduler\Logs' 


#### Add Jobs Here

# ReCept Monthly Export
@scheduler.task("cron", id="Recept Export", month='*', day=1)
def recept_export():
    # receptExport.export_report("Recept Export.json", trigger)
    print('ran recept~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    

# Crossroads Weekly Visit Export
@scheduler.task("cron", id="Crossroads Visit Export", day_of_week=0, hour=7, minute=00)
def crossroads_visits():
    # crossroadsExport.export_visits(output_log, 'configs/crossroads.ini', trigger)
    pass

# Crossroads Quarterly Provider Export
@scheduler.task("cron", id="Crossroads Provider Export", month='*/3' , day=1)
def crossroads_visits():
    # crossroadsExport.export_providers(output_log, 'configs/crossroads.ini' ,trigger)
    pass

# Nonfiler Import
@scheduler.task("cron", id="Nonfiler Import", day_of_week="mon-fri", hour=6, minute=00)
def nonfiler_import():
    # nonfilerImport.import_nonfilers(output_log, 'configs/brick.ini', trigger)
    pass

# Ascentis ETL
@scheduler.task("cron", id="Ascentis ETL", day_of_week="mon-sun", hour=6, minute=00)
def ascentis_etl():
    # ascentisETL.load_ascentis(output_log, 'prod', 'configs/ascentis.ini', trigger)
    pass

# New Partnership Patient Roster
@scheduler.task("cron", id="New Partnership Patient Roster", month='*', day=1)
def recept_export():
    # .export_new_partnership_roster(output_log, 'configs/ochin.ini', trigger)
    pass

# New Partnership Patient Roster
@scheduler.task("cron", id="Partnership Measure Import", month='*', day=1)
def recept_export():
    # partnershipImports.import_partnership_measures(output_log, trigger)
    pass

@scheduler.task("cron", id="Partnership Eligibility Import", month='*', day=1)
def recept_export():
    # partnershipImports.import_partnership_elig_and_cap(output_log, trigger)
    pass