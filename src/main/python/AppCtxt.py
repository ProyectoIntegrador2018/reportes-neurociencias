from fbs_runtime.application_context.PyQt5 import ApplicationContext

appctxt = None

def APPCTXT():
    global appctxt
    if appctxt is None: 
        appctxt = ApplicationContext()

    return appctxt