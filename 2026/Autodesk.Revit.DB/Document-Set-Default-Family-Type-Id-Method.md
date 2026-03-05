# Document Set Default Family Type Id Method

Source: https://www.revitapidocs.com/2026/1f0d5aac-4602-b479-82b4-dc54a030c0a3.htm

---

| Document Set Default Family Type Id Method |
| --- |

Sets the default family type id for the given family category. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetDefaultFamilyTypeId(
	ElementId familyCategoryId,
	ElementId familyTypeId
)
```

```
Public Sub SetDefaultFamilyTypeId ( 
	familyCategoryId As ElementId,
	familyTypeId As ElementId
)
```

```
public:
void SetDefaultFamilyTypeId(
	ElementId^ familyCategoryId, 
	ElementId^ familyTypeId
)
```

```
member SetDefaultFamilyTypeId : 
        familyCategoryId : ElementId * 
        familyTypeId : ElementId -> unit 
```

#### Parameters

familyCategoryId [ElementId](Element-Id-Class.md)
:   The family category id.

familyTypeId [ElementId](Element-Id-Class.md)
:   The default family type id.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The family type id familyTypeId is invalid for the give family category familyCategoryId.  \-or\-  familyCategoryId is not a built in category or parameter Element ID. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
