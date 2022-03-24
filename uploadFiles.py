import dropbox
import os
from pathlib import Path

    # file exists

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for name in files:
                local_path = os.path.join(root, name)
                print(local_path)
                with open (local_path,'rb') as f:
                    dbx.files_upload(f.read(),file_to)
            # relative_path=os.path.relpath(my_file,file_from)
            # dropbox_path=os.path.join(file_to,relative_path)
            # # with open (local_path,'rb') as f:
            # #     dbx.files_upload(f.read(),dropbox_path,dropbox.files.WriteMode.overwrite)   

def main():
    access_token ='sl.BEY_mTmtWafefcpQoLiKjwSU5r111aYXNFLo4Mw9Lhfbym3NpQc_6aAEgIgQwojC-IA-aGClVfo5ACezf2o-fcoYC97eP4cX3A-FVpzEEpb0RFu8sTC6ElNJbga0xxfaNXU57Q1daMxT'
    transferData = TransferData(access_token)
    file_from = input("Enter the File Path to transfer ")
    file_to = input("Enter the full path to upload to Dropbox ")
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()             
