#!/usr/bin/env python3
import requests,os,subprocess,logging,datetime
from dotenv import load_dotenv

def fetch (owner,repo,branch,token):
    try:
        URL=f"https://api.github.com/repos/{owner}/{repo}/commits?sha={branch}"
        headers = {}
        params={'per_page':1}
        print(pat)

        if token:
            headers["Authorization"]= f"Bearer {token}"

        response=requests.get(URL,headers=headers,params=params)
        ssh_link=f"git@github.com:{owner}/{repo}.git"

        if (response.status_code==200):
            logging.info("API successfully read")
            #commit=response.json()
            commits=response.json()
            #print("Hellow")
            for com in commits:
                search_commit=com['sha']
                print(com['sha'])
                logging.info("commit id to be searched now")
                search_commit_file(search_commit,ssh_link)
        else:
            logging.error("could not read GITHUB API")
            print("error reading GITHUB API")
        # print(ssh_link)
    except Exception as e:
        print("Error accessing GITHUB API",e)
        logging.error(f"could not read GITHUB API,{e}")

def search_commit_file(search_commit,ssh_link):
    try:
        if os.path.exists("commit.txt"):
            with open(r'commit.txt','r') as fc:
                lines=fc.read()
                if search_commit in lines:
                    print("existing commit id", search_commit, "\n code will not be pushed")
                    logging.info(f"commit id exist in the memory,\n already upto date,{search_commit}")
                else:
                    print("creating a new entry for ",search_commit,"\n code will be pushed")
                    logging.info(f"new commit id found :,{search_commit},\n code will be pushed to server for deployment")
                    store_latest_commit(search_commit,ssh_link)
        else:
            fc=open(r'commit.txt','w')            

    except IOError as er:
        print("Problem reading file",er)
        logging.error(f"Problem reading file while searching the committid,{er}")
    
def store_latest_commit(search_commit,ssh_link):
    try:
        with open('commit.txt','a') as fw:
            fw.write(search_commit + "\n")
            logging.info(f"writing into file complete for id:{search_commit}")
            print(githome)
            try:
                subprocess.run(['sh', f"{githome}/scrip.sh", ssh_link, "/dev/null"], check=True)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error executing script: {e}")
                print(f"Error executing script: {e}")
    except IOError as err:
        print("Error Writing the file",err)
        logging.error(f"Error Writing the commits to file,{err}")
        

    

if __name__ == '__main__':
    load_dotenv('/home/avinjay/GIT/.env')
    pat=os.getenv('GITHUB_PAT')
    githome=os.getenv('GITHOME')
    if not pat or not githome:
        print("Error: Missing GITHUB_PAT or GITHOME in .env file.")
        exit(1) 
    without_fr_time=datetime.datetime.now()
    date_time=without_fr_time.strftime('%Y%m%d_%H%M%S')
    #log_filename = os.path.join(githome, f"filelogg{date_time}.log")
    logging.basicConfig(filename=f"filelogg{date_time}.log",format="%(asctime)s - %(levelname)s - %(message)s",level=logging.DEBUG,force=True,filemode='w')
    #logging.basicConfig(filename='filelogg.log',format="{asctime}-{level}-{message}",style='{',filemode='w')
    fetch("Avinjay","CICD_project1","main",pat)
    logging.info("Script execution completed")
    #print(os.getenv('GITHUB_PAT'))
