# CVEase

CVEase is a web application designed to streamline the process of managing resumes and candidates for small to medium-sized companies or internal recruitment teams within large companies in the internet industry. The project is built with Django and uses SQLite as the database. It is deployed using AWS Elastic Beanstalk.

## Features

1. **Resume Upload and Parsing**: Automatically extracts email and phone contact information, as well as the candidate's tech stack, from uploaded PDF resumes.
2. **Candidate Profiles**: Each candidate has a dedicated page displaying their tech stack with badges, links to their resume for online viewing, one-click interview invitation, interview cancellation, and feedback from interviewers, HR, or hiring managers.
![Candidate profile page] (./cv/static/cv/images/cv-detail-page.png)
3. **Interview Scheduling**: Automatically sends an invitation email with interview details when HR selects the interview date, time, and position.
4. **Tech Stack Matching**: Identifies candidates with relevant tech stacks and ranks search results based on the number of matching skills.


## Dependencies and Libraries

- **asgiref**: Provides ASGI support for Django.
- **Django**: The web framework used to build the application.
- **Pillow**: Used for image processing tasks.
- **PyMuPDF**: Used for parsing PDF files to extract candidate information.
- **PyMuPDFb**: Another variant of PyMuPDF for additional functionality.
- **sqlparse**: Used for parsing SQL statements.

## Database Schema

- **cv_tag**: Stores tech stack tags related to candidates.
- **cv_candidate**: Stores candidate information, including name, resume file, email, phone, status, etc.
- **cv_candidate_tags**: Stores the relationship between candidates and tags.
- **cv_note**: Stores feedback related to candidates, including user, text, candidate ID, and creation time.
- **cv_invitation**: Stores interview invitation information, including candidate ID, position ID, and interview date.
- **cv_position**: Stores position information, including position title.

## Deployment

The application is deployed using AWS Elastic Beanstalk. 

## License

CVEase is licensed under the GNU General Public License v3.0. You may not use this code for commercial purposes without complying with the terms of this license.

# CVEase

CVEase 是一个 web 应用程序，旨在帮助互联网行业的中小型公司或大公司的内部招聘团队轻松管理简历和候选人信息。该项目使用 Django 构建，并使用 SQLite 作为数据库。它通过 AWS Elastic Beanstalk 部署。

## 功能

1. **简历上传和解析**：自动提取上传的 PDF 简历中的邮箱和电话联系信息，以及候选人的技术栈。
2. **候选人档案**：每个候选人有一个专属页面，显示其技术栈词条、跳转 PDF 在线阅读、一键邀请候选人面试、取消面试、面试官或 HR 或招聘经理留下的反馈并展示反馈。
3. **面试安排**：当 HR 选择面试日期、时间和职位后，自动发送包含面试信息的邀请邮件。
4. **技术栈匹配**：识别系统内具有相关技术栈的候选人，并根据匹配的技能数量对搜索结果进行排名。

## 介绍

CVEase 旨在帮助 HR 部门高效管理候选人信息和安排面试。它提供了一个用户友好的界面，用于上传和解析简历、管理候选人档案和处理面试安排。该应用程序使用高级 Python web 框架 Django 构建，并通过 AWS Elastic Beanstalk 部署以实现可扩展性和可靠性。

## 依赖和库

- **asgiref**：提供 Django 的 ASGI 支持。
- **Django**：构建应用程序所用的 web 框架。
- **Pillow**：用于图像处理任务。
- **PyMuPDF**：用于解析 PDF 文件以提取候选人信息。
- **PyMuPDFb**：PyMuPDF 的另一个变体，用于附加功能。
- **sqlparse**：用于解析 SQL 语句。

## 数据库模式

- **cv_tag**：存储候选人的标签信息。
- **cv_candidate**：存储候选人信息，包括名字、简历文件、邮箱、电话、状态等。
- **cv_candidate_tags**：存储候选人与标签的关系。
- **cv_note**：存储针对候选人的笔记，包括用户、文本、候选人 ID 和创建时间。
- **cv_invitation**：存储面试邀请信息，包括候选人 ID、职位 ID 和面试日期。
- **cv_position**：存储职位信息，包括职位标题。

## 部署

该应用程序通过 AWS Elastic Beanstalk 部署。


## 许可证

CVEase 根据 GNU 通用公共许可证 v3.0 进行许可。未经遵守此许可证条款，您不得将此代码用于商业目的。



