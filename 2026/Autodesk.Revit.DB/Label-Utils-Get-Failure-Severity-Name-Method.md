# Label Utils Get Failure Severity Name Method

Source: https://www.revitapidocs.com/2026/4492bdf0-a671-14e2-5836-ec920cda69a5.htm

---

| Label Utils Get Failure Severity Name Method |
| --- |

Gets the user\-visible name for the Severity of a Warning 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static string GetFailureSeverityName(
	FailureSeverity failureSeverity
)
```

```
Public Shared Function GetFailureSeverityName ( 
	failureSeverity As FailureSeverity
) As String
```

```
public:
static String^ GetFailureSeverityName(
	FailureSeverity failureSeverity
)
```

```
static member GetFailureSeverityName : 
        failureSeverity : FailureSeverity -> string 
```

#### Parameters

failureSeverity [FailureSeverity](d0cdffe3-22c5-b764-8090-5104f044b000.htm)
:   The Severity enum value

#### Return Value

String 
Returns the user\-visible name for the Severity of a Warning. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The name is obtained in the current Revit language. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[LabelUtils Class](Label-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
