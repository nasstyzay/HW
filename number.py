from pprint import pprint
import csv
import re


def normalize_phone_number(phone):
    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(?:\s*(доб.)\s*(\d+))?"
    replacement = r"+7(\2)\3-\4-\5"
    corrected_phone = re.sub(pattern, replacement, phone)

    match = re.search(pattern, phone)
    if match and match.group(6):
        corrected_phone += f" {match.group(6)}{match.group(7)}"
    return corrected_phone

def process_contacts_list(contacts_list):
    for contact in contacts_list:
        full_name = " ".join(contact[:3]).split(" ")
        while len(full_name) < 3:
            full_name.append("")
        contact[:3] = full_name[:3]

        contact[5] = normalize_phone_number(contact[5])


    unique_contacts = {}
    for contact in contacts_list:
        if tuple(contact[:3]) not in unique_contacts:
            unique_contacts[tuple(contact[:3])] = contact
        else:
            for i in range(len(contact)):
                if contact[i] != "":
                    unique_contacts[tuple(contact[:3])][i] = contact[i]

    return list(unique_contacts.values())


contacts_list = []
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


processed_contacts_list = process_contacts_list(contacts_list)


with open("phonebook_processed.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(processed_contacts_list)