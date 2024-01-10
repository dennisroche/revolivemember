import os
import sys

from streamlit import cli

base_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(base_path)

def deploy_streamlit():
    sys.argv = [
        "streamlit",
        "run",
        f"{base_path}/dashboard.py",
        "--server.port=8080",
        "--server.address=0.0.0.0",
    ]
    sys.exit(cli.main())