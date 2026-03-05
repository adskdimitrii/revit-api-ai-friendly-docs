# Building Operating Year Schedule Create Method

Source: https://www.revitapidocs.com/2026/dc482205-3384-6a11-0937-290acb36ee73.htm

---

| Building Operating Year Schedule Create Method |
| --- |

Creates a valid BuildingOperatingYearSchedule with the given name, where every day has the schedule daySchedule. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static BuildingOperatingYearSchedule Create(
	Document document,
	BuildingOperatingDaySchedule daySchedule,
	string name
)
```

```
Public Shared Function Create ( 
	document As Document,
	daySchedule As BuildingOperatingDaySchedule,
	name As String
) As BuildingOperatingYearSchedule
```

```
public:
static BuildingOperatingYearSchedule^ Create(
	Document^ document, 
	BuildingOperatingDaySchedule^ daySchedule, 
	String^ name
)
```

```
static member Create : 
        document : Document * 
        daySchedule : BuildingOperatingDaySchedule * 
        name : string -> BuildingOperatingYearSchedule 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document to create this BuildingOperatingYearSchedule for.

daySchedule [BuildingOperatingDaySchedule](b9a7693c-e3ae-72d0-8d15-b377025b90b7.htm)
:   A schedule to assign to every day.

name String
:   The intended schedule name, may be modified to disambiguate with existing elements.

#### Return Value

[BuildingOperatingYearSchedule](18d6fc71-5801-04cf-082d-4deb26b7756b.htm) 
The newly created BuildingOperatingYearSchedule. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element daySchedule was not found in the given document.  \-or\-  name cannot include prohibited characters, such as "{, }, \[, ], \|, ;, less\-than sign, greater\-than sign, ?, \`, \~".  \-or\-  name must be trimmed.  \-or\-  name is an empty string or contains only whitespace. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BuildingOperatingYearSchedule Class](18d6fc71-5801-04cf-082d-4deb26b7756b.htm) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
