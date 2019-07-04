import os
#from library._1_simple import app
#from library._2_HTML import app
#from library._3_templet import app
#from library._4_extern_temp import app
#from library._5_routing import app
#from library._6_error import app
#from library._7_req import app
#from library._8_redirects import app
#from library._9_simple_database import app
#from library._10_jinja2 import app
#from library._11_database_app_template_conditional import app
#from library._12_database_app_with_join import app
# from library._13_form import app
# from library._14_static_files import app
from library._15_base import app

if __name__ == "__main__":
    app.debug = True
    host = os.environ.get('IP','0.0.0.0')
    port = int(os.environ.get('PORT',8088))
    app.run (host = host,port = port)
