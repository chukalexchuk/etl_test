create table if not exists account (
    holidayDate date not null,
    localName varchar (50) not null,
    globalName varchar (50) not null,
    countryCode varchar (50) not null,
    fixed bool,
    globalHoliday bool,
    counties varchar (50),
    launchYear int,
    types varchar (50)
);