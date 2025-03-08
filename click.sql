create proc clickin
@employeeid int
as 
BEGIN
declare @firstname nvarchar(20)
declare @lastname nvarchar(20)
if exists(select 1 from employeetbl where employeeid= @employeeid)
select @firstname = firstname from employeetbl
where employeeid = @employeeid

select @lastname = lastname from employee tbl 
where  @employeeid = @employeeid

insert into labortime (employeeid, fristname, lastname, clickintime)
VALUES (@employeeid , @firstname ,@lastname,gatedate() )

end;