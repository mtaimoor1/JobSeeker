# How to deploy locally
Create virtual environment and install the dependencies
```bash
pip install -r requirments.txt
```
After installing the dependencies add the following environment variable in your terminal using the following command
```bash
export aws_access_key="<your_aws_access_key>"
export aws_secret_key="<your_aws_secret_key>"
export PYHTONPATH=<path_to_your_local_repo>
```
If you're running it using PyCharm, then add these variable to the path using Run Configuration of main.py i.e. *right click main.py > Modify Run Configuration > Copy to Environment Variable section*
