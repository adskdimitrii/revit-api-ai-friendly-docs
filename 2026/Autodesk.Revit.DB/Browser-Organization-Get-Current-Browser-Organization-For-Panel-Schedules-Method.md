# Browser Organization Get Current Browser Organization For Panel Schedules Method

Source: https://www.revitapidocs.com/2026/9488ac90-2894-62ec-1b4b-b9aa1109fdc4.htm

---

| Browser Organization Get Current Browser Organization For Panel Schedules Method |
| --- |

Gets the [BrowserOrganization](Browser-Organization-Class.md) that applies to the Panel Schedules section of the project browser. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static BrowserOrganization GetCurrentBrowserOrganizationForPanelSchedules(
	Document document
)
```

```
Public Shared Function GetCurrentBrowserOrganizationForPanelSchedules ( 
	document As Document
) As BrowserOrganization
```

```
public:
static BrowserOrganization^ GetCurrentBrowserOrganizationForPanelSchedules(
	Document^ document
)
```

```
static member GetCurrentBrowserOrganizationForPanelSchedules : 
        document : Document -> BrowserOrganization 
```

#### Parameters

document [Document](Document-Class.md)
:   Revit document from which to get the organization data.

#### Return Value

[BrowserOrganization](Browser-Organization-Class.md) 
The BrowserOrganization for panel schedules, or null if no panel schedules sections exist. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BrowserOrganization Class](Browser-Organization-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
