use schoolmanagementsystem;
select * from studentpor;

select count(Medu) from studentpor;

select distinct Medu, count(Medu) from studentpor group by Medu order by Medu;
select max(age) from studentpor;

select Fjob, max(age) from studentpor group by Fjob order by Fjob