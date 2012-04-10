import json
import os
import re


def main():
    new_source = "source/journal"

    years_path = "source.old"
    years = os.listdir(years_path)
    years.sort()

    counter = 0

    for year in years:

        months_path = years_path + "/" + year
        months = os.listdir(months_path)
        months.sort()

        for month in months:

            days_path = months_path + "/" + month
            days = os.listdir(days_path)
            days.sort()

            for single in days:

                files_path = days_path + "/" + single
                files = os.listdir(files_path)
                files.sort()

                for post in files:
                    post_path = files_path + "/" + post

                    f = open(post_path, "rb")
                    content = f.read()

                    metadata_search = re.search("<!-- METADATA: (.+) -->", content, re.DOTALL)
                    metadata = json.loads(metadata_search.group(1))
                    content = content.replace(metadata_search.group(0), '')

                    title_string = "Title: %s\n" % metadata['title']
                    date_string = "Date: %s\n" % metadata['time']
                    slug_string = "Slug: %s\n" % post.split('.')[0]

                    title_search = re.match("### (.+)", content)
                    content = content.replace(title_search.group(0), '')
                    content = content.strip()

                    counter_string = str(counter)
                    if len(counter_string) < 4:
                        dif = 4 - len(counter_string)
                        counter_string = "0" * dif + counter_string

                    new_file_path = "%s/%s-%s" % (new_source, counter_string, post)
                    new_file = open(new_file_path, "wb")

                    new_file.write(title_string)
                    new_file.write(date_string)
                    new_file.write(slug_string)
                    new_file.write("\n")
                    new_file.write(content)
                    new_file.close()

                    counter += 1


if __name__ == "__main__":
    main()
