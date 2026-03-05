# Numbering Schema Change Number Method

Source: https://www.revitapidocs.com/2026/dc93cd7f-dc11-45da-3ed6-c459d1c55c97.htm

---

| Numbering Schema Change Number Method |
| --- |

Replaces an existing number with a new one (that does not exist yet). 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<ElementId> ChangeNumber(
	string partition,
	int fromNumber,
	int toNumber
)
```

```
Public Function ChangeNumber ( 
	partition As String,
	fromNumber As Integer,
	toNumber As Integer
) As IList(Of ElementId)
```

```
public:
IList<ElementId^>^ ChangeNumber(
	String^ partition, 
	int fromNumber, 
	int toNumber
)
```

```
member ChangeNumber : 
        partition : string * 
        fromNumber : int * 
        toNumber : int -> IList<ElementId> 
```

#### Parameters

partition String
:   Name of the partition that identifies the sequence containing the number to be changed.

fromNumber Int32
:   Number to be changed; there must already be an element with that number in the sequence.

toNumber Int32
:   Number to change to; no element must have this number yet in the sequence.

#### Return Value

IList [ElementId](Element-Id-Class.md) 
A collection of elements affected by the change of the number ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The sequence partition does not exist in the schema.  \-or\-  The specified sequence does not contain any elements with the given fromNumber.  \-or\-  There already are elements with the given toNumber in the specified sequence. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The value of toNumber must be in the range from 1 to the maximum value for an Integer type |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Either the schema or its document cannot be modified at present.  \-or\-  Can't access the number while an async operation is running. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method gives the caller the ability to overwrite any number used in a given
 numbering sequence as long as the new number does not exist in the same sequence yet.
 If an attempt is made to replace a number by another that already exists, an exception
 will be thrown. 

The new number will automatically be applied to all elements that bear the original
 number, thus those elements must be free to be modified. A collection of element Ids
 of all the affected elements is returned by this method. 

The method is independent of the sequence's current starting number that might have
 been assigned previously, meaning that the new number will be accepted even if it is
 lower than the previously set start number in the sequence. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[NumberingSchema Class](Numbering-Schema-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
