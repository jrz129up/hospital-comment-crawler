import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import os
import glob
import csv

def get_province_urls(base_url):
    province_urls = []
    headers = {
    hidden headers
    }
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        divs = soup.find_all('div', class_=['kstl','kstl2'])
        for div in divs:
            a = div.find('a')
            if a:
                href = a['href']
                full_url = f"https:{href}" if href.startswith("//") else f"http:{href}"
                province_name = a.get_text(strip=True)
                province_urls.append((province_name, full_url))
    return province_urls

def get_area_hospitals_info(name, url):
    headers = {
    hidden headers
    }
    response = requests.get(url,headers=headers)
    if response.status_code != 200:
        print(f"Error retrieving {url}")
        return []
    soup = BeautifulSoup(response.content, 'html.parser')
    m_box_green = soup.find('div', class_='m_box_green')
    ct = m_box_green.find('div', class_='ct') if m_box_green else None
    if not ct:
        print("No 'ct' div found.")
        return []

    m_title_greens = ct.find_all('div', class_='m_title_green')
    m_ctt_greens = ct.find_all('div', class_='m_ctt_green')

    area_hospitals_info = []

    codes
        for hospital in hospitals:
            a = hospital.find('a')
            span = hospital.find('span')
            if a and span:
                hospital_name = a.get_text(strip=True)
                hospital_url = a['href']
                hospital_type = span.get_text(strip=True)
                area_hospitals_info.append({
                    'province_name': name,
                    'area_name': area_name,
                    'hospital_name': hospital_name,
                    'hospital_url': hospital_url,
                    'hospital_type': hospital_type
                })
                print(hospital_name)
    return area_hospitals_info

def parse_hospital_id(url):
    hospital_id = url.split('/')[-1].split('.')[0]
    return hospital_id

def post_and_parse_comments(hospital_url, comment_type):
    hospital_id = parse_hospital_id(hospital_url)
    post_url = "ajax"
    headers = {
    hidden headers
    }

    payload = {
        'hospitalId': hospital_id,
        'diseaseId': 0,
        'hospitalFacultyId': '',
        'commentType': comment_type,  # 1表示好评，2表示差评
        'page': 1
    }

    response = requests.post(post_url, data=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    total_pages = data['pageInfo'].get('totalPage', 0)
    total_comdata = data['pageInfo'].get('total', 0)
    if total_pages == 0 or total_comdata == 0:
        return [], total_comdata
    results = []
    k=0
    for page in range(1, total_pages + 1):
        payload['page'] = page
        response = requests.post(post_url, data=payload,headers=headers)
        data = response.json()
        time.sleep(0.2)
        print(k)
        k +=1
        for comment_info in data['commentInfoList']:
            patient_name = comment_info.get('patientName', '')
            comment_Id = comment_info.get('commentId', '')
            efficacy = comment_info.get('efficacy','')
            attitude = comment_info.get('attitude', '')
            disease_Desc = comment_info.get('diseaseDesc','')
            disease_tag = comment_info.get('diseaseTag', '')
            doctor_name = comment_info['doctorInfo'].get('name', '')
            doctor_grade = comment_info['doctorInfo'].get('grade', '')
            doctor_Id= comment_info['doctorInfo'].get('doctorId', '')
            comment_data = {
                'province_name': hospital_info['province_name'],
                'area_name': hospital_info['area_name'],
                'hospital_name': hospital_info['hospital_name'],
                'hospital_type': hospital_info['hospital_type'],
                'comment_type': comment_type,
                'patient_name': patient_name,
                'efficacy': efficacy,
                'attitude':attitude,
                'disease_Desc': disease_Desc,
                'disease_tag': disease_tag,
                'doctor_name': doctor_name,
                'doctor_grade': doctor_grade,
                'doctor_ID': doctor_Id,
                'comment_ID': comment_Id,
            }
            results.append(comment_data)
    cleaned_results = []
    for comment_data in results:
        some codes

    return cleaned_results, total_comdata

def save_to_csv(results, filename):
    if not results:
        print(f"No data to write for {filename}.")
        return
    with open(filename, 'w', newline='', encoding='utf_8_sig') as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

base_url = "https://www.haodf.com/hospital/list.html"
total_comments_count = 0
province_urls = get_province_urls(base_url)
essential loops:
    hospitals = get_area_hospitals_info(province_name, province_url)
    all_hospitals.extend(hospitals)
    print(province_name)
    for hospital_info in all_hospitals:
        hospital_url = hospital_info['hospital_url']
        good_comments, good_total = post_and_parse_comments(hospital_url, '1')
        bad_comments, bad_total = post_and_parse_comments(hospital_url, '2')
        if good_total > 0:
            total_comments_count += good_total
        if bad_total > 0:
            total_comments_count += bad_total
        print(f"total: {total_comments_count}")
        if good_comments or bad_comments:
            comments = good_comments + bad_comments
            csv_filename = f"{hospital_info['hospital_name']}.csv"
            save_to_csv(comments, f"{province_subcomments_path}{csv_filename}")
            print(f"{hospital_info['hospital_name']} done")
        else:
            print(f"No comments found for {hospital_info['hospital_name']}.")

    all_files = glob.glob(os.path.join(province_subcomments_path, "*.csv"))
    all_comments_df = pd.DataFrame()

    for f in all_files:
        try:
            temp_df = pd.read_csv(f)
            if not temp_df.empty:
                all_comments_df = pd.concat([all_comments_df, temp_df], ignore_index=True)
            else:
                print(f"Skipped {f}: File contains no data")
        except pd.errors.EmptyDataError:
            print(f"Skipped {f}: No columns to parse from file")
        except Exception as e:
            print(f"Skipped {f}: Error occurred - {e}")
    all_comments_df.to_csv(f"{province_name}.csv", index=False, encoding='utf_8_sig')

province_comments_path = 'path'
province_files = glob.glob(os.path.join(province_comments_path, "*.csv"))
all_comments_combined_df = pd.DataFrame()
for file_path in province_files:
    current_province_df = pd.read_csv(file_path)
    if not current_province_df.empty:
        all_comments_combined_df = pd.concat([all_comments_combined_df, current_province_df], ignore_index=True)
all_comments_combined_df.to_csv('csv', index=False, encoding='utf_8_sig')
print('done')

dfj = pd.read_csv('csv')
df_filtered = dfj[dfj['patient_name'].str.contains(r'\[.*?\]', na=False)].copy()
df_filtered['origin_name'] = df_filtered['patient_name'].str.extract(r'\[(.*?)\]', expand=False)
new_columns_order = ['comment_ID', 'doctor_ID', 'area_name', 'origin_name'] + [col for col in df_filtered.columns if col not in ['comment_ID', 'doctor_ID', 'area_name', 'origin_name']]
df_filtered = df_filtered[new_columns_order]
df_sorted = df_filtered.sort_values(by=['comment_ID'])
df_sorted.to_csv('csv', index=False)

print(f'Total comments collected: {total_comments_count}')
