# Building Operating Day Schedule Get Value For Hour Method

Source: https://www.revitapidocs.com/2026/f73beefa-df3a-68dd-775f-3bd2d79eb97f.htm

---

| Building Operating Day Schedule Get Value For Hour Method |
| --- |

Gets the usage value for an hour. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double GetValueForHour(
	int hour
)
```

```
Public Function GetValueForHour ( 
	hour As Integer
) As Double
```

```
public:
double GetValueForHour(
	int hour
)
```

```
member GetValueForHour : 
        hour : int -> float 
```

#### Parameters

hour Int32
:   The hour in the day, as an integer. For example: 0 is 12:00 midnight to 1:00 am, 6 is 6:00 am to 7:00 am, 12 is 12:00 noon to 1:00 pm, and 23 is 11:00 pm to midnight.
 To avoid issues around daylight savings times, these hours represent 1/24 of an earth rotation, and will not be exactly 60 minutes.

#### Return Value

Double 
The usage as a fraction between 0 and 1 inclusive. For example: 0 in a lighting schedule means all lights are off, .5 means half of lights are on, 1 means all lights are on. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | hour must be from 0 to 23 inclusive. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BuildingOperatingDaySchedule Class](b9a7693c-e3ae-72d0-8d15-b377025b90b7.htm) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
