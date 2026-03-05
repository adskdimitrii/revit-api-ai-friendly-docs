# Rebar Trim Extend Data Get Added Bar Geometry Method

Source: https://www.revitapidocs.com/2026/64c06ae1-86b7-4e86-94df-2a6d99084a11.htm

---

| Rebar Trim Extend Data Get Added Bar Geometry Method |
| --- |

Gets the added curves that will represent the bar at index barIndex. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<Curve> GetAddedBarGeometry(
	int barIndex
)
```

```
Public Function GetAddedBarGeometry ( 
	barIndex As Integer
) As IList(Of Curve)
```

```
public:
IList<Curve^>^ GetAddedBarGeometry(
	int barIndex
)
```

```
member GetAddedBarGeometry : 
        barIndex : int -> IList<Curve> 
```

#### Parameters

barIndex Int32
:   The index of the bar. Should be a number between 0 and GetNumberOfBarGeometry() \- 1\.

#### Return Value

IList [Curve](../Autodesk.Revit.DB/Curve-Class.md) 
Returns the curves that will represent the bar at index barIndex. The terminations' plane normals will be applied on these curves. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barIndex is not in the range \[ 0, GetNumberOfBarGeometry()\-1 ]. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarTrimExtendData Class](980b816d-dc7e-7550-3e37-61482516b5ab.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
