from os import environ
from dotenv import load_dotenv

class Config():
    def __init__(self):
        load_dotenv()

    def vsphere_host(self):
        return self.vsphere_server_details().get('host')

    def vsphere_server_details(self):
        return {
                    "host"    : environ.get('VSPHERE_HOST'),
                    "username": environ.get('VSPHERE_USERNAME'),
                    "password": environ.get('VSPHERE_PASSWORD')
                }

    def vm_account(self):
        return  {
                    "username": environ.get('VM_USERNAME'),
                    "password": environ.get('VM_PASSWORD')
                }