# parsing of website https://www.timesjobs.com/
# -> only fresh vacancies of Python language

from bs4 import BeautifulSoup
import requests, time

# User input questions
print('Type skills which you do not have')
unfamiliar_skills = input('>> ')
print('Type of format of result txt/json: ')
format_file = input('>> ').lower()
print(f'Result of {unfamiliar_skills}')


# whole function for webpage
def find_work():
    # gain the whole structure code html
    html_text_output = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup_work = BeautifulSoup(html_text_output, 'lxml')
    # will return all jobs in first page with class ->
    jobs = soup_work.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # will show numeration of job
    for index, job in enumerate(jobs):
        # fresh job condition
        job_published_date = job.find('span', class_='sim-posted').span.text
        # condition for fresh job position
        if 'few' in job_published_date:

            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            link_to_detail_info = job.header.h2.a['href']

            # condition if user select file format json from input
            if unfamiliar_skills not in skills and format_file == "json":
                with open(f'results/{index}.json', 'w') as file:
                    file.write(f'Company Name: {company_name.strip()}')
                    file.write(f'Required Skills: {skills.strip()}')
                    file.write(f'More Info: {link_to_detail_info}')
                print(f'File saved: {index}')

            # condition if user select file format txt from input
            if unfamiliar_skills not in skills and format_file == "txt":
                with open(f'results/{index}.txt', 'w') as file:
                    file.write(f'Company Name: {company_name.strip()}')
                    file.write(f'Required Skills: {skills.strip()}')
                    file.write(f'More Info: {link_to_detail_info}')
                print(f'File saved: {index}')


# time for waiting
if __name__ == '__main__':
    while True:
        find_work()
        time_wait = 10
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)
