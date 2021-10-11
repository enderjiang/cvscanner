
INTRODUCTION
------------
Recently our company has started to recruit oversea staff and new interns. And due to the massive respond, our team has been overloaded in screening and interviewing applicants. There are many good applicants but it’s unlikely we can read through their resume in details one by one. Platform like linkedin doesn’t provide a friendly window to help us further screen applicant, and other AI based platforms are not smart enough, so I decide to do one version that fits our own needs.
This program is written mainly for massive cv check, but you may also use it for some other information searching and organizing.

When we do resume screening, we will look at some keywords like years of experience, MNC name, software skills, but everyone has their style in writing. It’s not possible to always capture the words by our eyes. So we would use this tool to do massive screening and extract the keywords. When we run multiple screening and get an organized result, we can also quickly find out which candidate fulfill most of our keywords.

When the company only receive 10 applicants per year, we have bandwidth to do it one by one, but now we receive 50-100 applicants over a week’s time from each county, and automation is more important.

So I wrote this mini program using python and some general library to help us speed up this process.
For any program manager, or teamleader, you’ll be starting to look at resources and recruiting new teammates, I hope this program can help you to do some initial screening so as to save some time. We are still updating this program, do provide us feedback so we can improve further.


VERSION 1.1.6
------------
Massive pdf check Keywords searching Csv organizing


CONFIGURATION
-------------
please drop all resumes into the [CV] folder before the analysis


START
-------------
you can choose the search mode.
1.	Search random keywords

If you want to search random content, then your input should be single word or short phrase to get accurate result, like"annual revenue" "python","sales","intel"')
You can search as many times as you want, and the program will organize the full result at the end of this program
 

2.	Search via a given list (for example you can create a list with skills, company names, etc to do cross checking)

If you would like to do a list search, please drop a info.csv file in [Infocsv] Folder, keep all data in one row

 
At the end of this program it will provide the search result, organize the name together, and write all result to the csv file in [CVresult] Folder

After you press X, this program Will Self-Destruct in Five Seconds...

