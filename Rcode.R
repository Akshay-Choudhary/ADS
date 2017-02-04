# Min, Max, Median, Avg for GPA and YearofWorkExp

collegeData <- read.csv("ClassData.csv") #import Data
attach(collegeData)

min(GPA)#minimum
max(GPA) #maximum
median(GPA) #median
mean(GPA) #average 

min(Years.of.work.experience) #minimum
max(Years.of.work.experience) #maximum
median(Years.of.work.experience) #median
mean(Years.of.work.experience) #average

# 2. Find mode of salary

data <- read.csv("ClassData.csv")
getmode <- function(v) {
  +     uniqv <- unique(v)
  +     uniqv[which.max(tabulate(match(v, uniqv)))]
  + }
result <- getmode(data$Latest.salary..per.year.)
result

#3.% of students having Co/op and not having Co/op
coop <- toupper(data$Coops.Internships..YN.)

coop_yes <- length(which(coop=="Y"))
coop_no <- length(which(coop=="N"))

perc_yes <- coop_yes/coop * 100

#4. Find No of students with more than 500 LinkedIn contacts
count <- length(which(data$Number.of.contacts.on.Linkedin > 500))
count

#5. Find the Inter Quartile Range for the Expected Salalry Range?
IQR(data$Expected.Salary.after.graduation)