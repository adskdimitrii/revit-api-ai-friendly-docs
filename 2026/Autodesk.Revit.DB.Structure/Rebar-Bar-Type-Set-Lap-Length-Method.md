# Rebar Bar Type Set Lap Length Method

Source: https://www.revitapidocs.com/2026/40db2d4a-622e-da37-cd5f-ffba541474b3.htm

---

| Rebar Bar Type Set Lap Length Method |
| --- |

Sets the lap length for the specified Rebar Splice Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetLapLength(
	ElementId rebarSpliceTypeId,
	double lapLength
)
```

```
Public Sub SetLapLength ( 
	rebarSpliceTypeId As ElementId,
	lapLength As Double
)
```

```
public:
void SetLapLength(
	ElementId^ rebarSpliceTypeId, 
	double lapLength
)
```

```
member SetLapLength : 
        rebarSpliceTypeId : ElementId * 
        lapLength : float -> unit 
```

#### Parameters

rebarSpliceTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Splice Type id.
 Interactions with Rebar Splice Types can be done with the functions in [RebarSpliceTypeUtils](98b9e51e-cd97-954d-4a31-a5189696b27e.htm) .

lapLength Double
:   The new value of the lap length.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarSpliceTypeId doesn't represent a valid Rebar Splice Type. It should be an ElementType of BuiltInCategory.OST\_RebarSpliceType category.  \-or\-  For the specified Rebar Splice Type the lap length is auto calculated and the lap length cannot be manually set.  Its value is computed based on the formula splice type: lap length multiplier \* bar nominal diameter. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for lapLength must be non\-negative. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
