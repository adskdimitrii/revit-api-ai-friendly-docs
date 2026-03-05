# Building Operating Day Schedule Set Value For Hour Method

Source: https://www.revitapidocs.com/2026/7b251879-4b7c-05c1-b50d-0b28f8da1b8d.htm

---

| Building Operating Day Schedule Set Value For Hour Method |
| --- |

Sets the usage value for an hour. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetValueForHour(
	int hour,
	double usage
)
```

```
Public Sub SetValueForHour ( 
	hour As Integer,
	usage As Double
)
```

```
public:
void SetValueForHour(
	int hour, 
	double usage
)
```

```
member SetValueForHour : 
        hour : int * 
        usage : float -> unit 
```

#### Parameters

hour Int32
:   The hour in the day, as an integer. For example: 0 is 12:00 midnight to 1:00 am, 6 is 6:00 am to 7:00 am, 12 is 12:00 noon to 1:00 pm, and 23 is 11:00 pm to midnight.
 To avoid issues around daylight savings times, these hours represent 1/24 of an earth rotation, and will not be exactly 60 minutes.

usage Double
:   The usage as a fraction between 0 and 1 inclusive. For example: 0 in a lighting schedule means all lights are off, .5 means half of lights are on, 1 means all lights are on.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | hour must be from 0 to 23 inclusive.  \-or\-  The given value for usage must be non\-negative.  \-or\-  usage should be less than or equal to 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BuildingOperatingDaySchedule Class](b9a7693c-e3ae-72d0-8d15-b377025b90b7.htm) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
