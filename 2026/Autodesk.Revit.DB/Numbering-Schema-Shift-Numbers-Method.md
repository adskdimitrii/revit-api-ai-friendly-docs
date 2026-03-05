# Numbering Schema Shift Numbers Method

Source: https://www.revitapidocs.com/2026/8962e7e3-0860-acd5-c488-d8f93867b1c1.htm

---

| Numbering Schema Shift Numbers Method |
| --- |

Shifts all numbers in the sequence so the starting number has the given value. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ShiftNumbers(
	string partition,
	int firstNumber
)
```

```
Public Sub ShiftNumbers ( 
	partition As String,
	firstNumber As Integer
)
```

```
public:
void ShiftNumbers(
	String^ partition, 
	int firstNumber
)
```

```
member ShiftNumbers : 
        partition : string * 
        firstNumber : int -> unit 
```

#### Parameters

partition String
:   Name of the partition that identifies the sequence. The sequence must exist.

firstNumber Int32
:   Value for the new first (lowest) number of the sequence.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The sequence partition does not exist in the schema. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | firstNumber must be in range between 1 and MaximumStartingNumber. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Either the schema or its document cannot be modified at present.  \-or\-  Can't access the number while an async operation is running. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A shift of all numbers in the sequence will be computed and applied
 so the first (lowest) number in the sequence would have the given value.
 All the other numbers will then be shifted relatively by the same amount. 

Any existing gaps in the current numbering sequence will be preserved. 

Shifts that would make the start number less than 1 or bigger than [MaximumStartingNumber](f7a8b906-ee60-2a71-bc1a-30fa81b4f299.htm) are considered invalid. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[NumberingSchema Class](Numbering-Schema-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
