### Metsenat Club API Links:

* api/v1/sponsor/register/ - REGISTER SPONSOR (POST)
* api/v1/sponsors/ - LIST SPONSORS (GET)
* api/v1/sponsor/1/ - DETAIL SPONSOR (GET)
* api/v1/sponsor/update/1/ - UPDATE SPONSOR (PUT)

SPONSOR FILTERS:

* api/v1/sponsors/?search=Alimov - SEARCH BY NAME
* api/v1/sponsors/?status=yangi - FILTER BY STATUS
* api/v1/sponsors/?balance=30000000 - FILTER BY BALANCE

UNIVERSITY:

* api/v1/university/create/ - CREATE UNIVERSITY

STUDENT:

* api/v1/student/register/ - REGISTER STUDENT
* api/v1/students/ - LIST STUDENTS
* api/v1/student/1/ - DETAIL STUDENT
* api/v1/student/update/1/ - UPDATE STUDENT

STUDENT FILTERS:

* api/v1/students/?search=jakhongir - SEARCH BY NAME
* api/v1/students/?student_type=magistr - FILTER BY TYPE
* api/v1/students/?university=1 - FILTER BY UNIVERSITY

STUDENT SPONSORS:

* api/v1/student/sponsor/create - CREATE STUDENT SPONSORS
* api/v1/student/sponsor/update/1/ - UPDATE STUDENT SPONSOR

DASHBOARD:

* dashboard/ - LIST DASHBBOARD
* dashboard/students - STUDENT DATA FOR LINE CHART
* dashboard/sponsors - SPONSOR DATA FOR LINE CHART