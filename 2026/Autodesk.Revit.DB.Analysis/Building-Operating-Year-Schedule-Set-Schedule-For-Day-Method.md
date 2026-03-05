# Building Operating Year Schedule Set Schedule For Day Method

Source: https://www.revitapidocs.com/2026/904d2cfb-6f50-4922-8ee9-681dc6b5f73d.htm

---

| Building Operating Year Schedule Set Schedule For Day Method |
| --- |

Sets the BuildingOperatingDaySchedule for this day of the year. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetScheduleForDay(
	DateTime day,
	BuildingOperatingDaySchedule daySchedule
)
```

```
Public Sub SetScheduleForDay ( 
	day As DateTime,
	daySchedule As BuildingOperatingDaySchedule
)
```

```
public:
void SetScheduleForDay(
	DateTime day, 
	BuildingOperatingDaySchedule^ daySchedule
)
```

```
member SetScheduleForDay : 
        day : DateTime * 
        daySchedule : BuildingOperatingDaySchedule -> unit 
```

#### Parameters

day DateTime
:   The day of the year. The value must be in 2023 (the template year) and have the time zone set to gmt/utc.
 Time values will be ignored.

daySchedule [BuildingOperatingDaySchedule](b9a7693c-e3ae-72d0-8d15-b377025b90b7.htm)
:   The schedule used on that day.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | daySchedule must be in the same document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | day must be in the year 2023\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The day argument must be in 2023 to match the template year in the user interface calendar: it has 365 days and starts on a Sunday. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BuildingOperatingYearSchedule Class](18d6fc71-5801-04cf-082d-4deb26b7756b.htm) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
