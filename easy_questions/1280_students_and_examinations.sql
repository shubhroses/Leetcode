select 
    st.student_id,
    st.student_name,
    sb.subject_name,
    count(e.student_id) as attended_exams
from Students st
join Subjects sb
left join Examinations e
    on sb.subject_name = e.subject_name
    and st.student_id = e.student_id
group by st.student_id, sb.subject_name
order by st.student_id, sb.subject_name;