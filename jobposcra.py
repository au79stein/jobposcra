#!/usr/bin/env python3

import sys
import argparse
import urllib
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import os

def load_jobs(url, job_title, location):
    #// q=devops+engineer&l=remote&fromage=7
    #// q=devops+engineer&l=remote&fromage=last&sort=date
    getVars = {'q' : job_title, 'l' : location, 'fromage' : 'last', 'sort' : 'date'}
    url_line = (url + '?' + urllib.parse.urlencode(getVars))
    print(f"url_line: {url_line}")
    page = requests.get(url_line)
    soup = BeautifulSoup(page.content, "html.parser")
    print(f"soup: {soup}")
    job_soup = soup.find(id="resultsCol")
    print(f"job_soup: {job_soup}")
    return job_soup

#def find_jobs(url, job_title, location, specifications, filename="results.xls"):
def find_jobs(url, job_title, location):
    #job_soup = load_jobs(url, job_title, location)
    job_soup = load_jobs(url, "devops+engineer", "remote")
    print(job_soup)
    #jobs_list, num_listings = extract_job_info(job_soup, characs)
    
def main():
    if len(sys.argv) < 2:
        print(sys.argv)
        raise ValueError('usage: jobposcra <url>')
    url = sys.argv[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument('--read', action="store_true")

    args = parser.parse_args()
    print(f"url:  {args.url}")
    if args.read == True:
        print(f"read: {args.read}")

    find_jobs(url, "devops+engineer", "remote")

if __name__ == '__main__':
    main()
