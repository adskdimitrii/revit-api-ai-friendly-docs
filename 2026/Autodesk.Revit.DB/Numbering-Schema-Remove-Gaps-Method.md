# Numbering Schema Remove Gaps Method

Source: https://www.revitapidocs.com/2026/a97a1aff-4afe-7aa7-098a-f71229efdccd.htm

---

| Numbering Schema Remove Gaps Method |
| --- |

Removes gaps, if any, in a numbering sequence 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void RemoveGaps(
	string partition
)
```

```
Public Sub RemoveGaps ( 
	partition As String
)
```

```
public:
void RemoveGaps(
	String^ partition
)
```

```
member RemoveGaps : 
        partition : string -> unit 
```

#### Parameters

partition String
:   Name of the partition that identifies the sequence. The sequence must exist.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The sequence partition does not exist in the schema. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Either the schema or its document cannot be modified at present.  \-or\-  Can't access the number while an async operation is running. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Gaps are removed by shifting numbers above each gap down by the amount of
 numbers skipped in the gap. The lowest number in the sequence will remain unchanged. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[NumberingSchema Class](Numbering-Schema-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
