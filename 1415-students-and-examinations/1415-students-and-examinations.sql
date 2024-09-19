# Write your MySQL query statement below
select st.student_id, st.student_name, sb.subject_name, count(et.subject_name) as attended_exams
from students st join Subjects sb
left join Examinations et 
on st.student_id=et.student_id and et.subject_name=sb.subject_name
group by st.student_id, st.student_name, sb.subject_name
order by st.student_id, sb.subject_name;