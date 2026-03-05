# Temporary Graphics Manager Set Tooltip Method

Source: https://www.revitapidocs.com/2026/a154f11d-be30-c4ad-0a6d-1d6cb1bff1c1.htm

---

| Temporary Graphics Manager Set Tooltip Method |
| --- |

Sets the tooltip for the temporary graphics object. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetTooltip(
	int index,
	string tooltip
)
```

```
Public Sub SetTooltip ( 
	index As Integer,
	tooltip As String
)
```

```
public:
void SetTooltip(
	int index, 
	String^ tooltip
)
```

```
member SetTooltip : 
        index : int * 
        tooltip : string -> unit 
```

#### Parameters

index Int32
:   Unique index of the temporary graphics object to be updated.

tooltip String
:   Tooltip to be set.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | index is out of range of TemporaryGraphicsManager managed objects, or the indexed object has been removed from the document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[TemporaryGraphicsManager Class](Temporary-Graphics-Manager-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
