# Rebar Set Crank Type Id Method

Source: https://www.revitapidocs.com/2026/c45e2074-7675-2eb6-00f0-9e0794f262af.htm

---

| Rebar Set Crank Type Id Method |
| --- |

Sets the id of the Crank Type to be applied to the rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCrankTypeId(
	int end,
	ElementId crankTypeId
)
```

```
Public Sub SetCrankTypeId ( 
	end As Integer,
	crankTypeId As ElementId
)
```

```
public:
void SetCrankTypeId(
	int end, 
	ElementId^ crankTypeId
)
```

```
member SetCrankTypeId : 
        end : int * 
        crankTypeId : ElementId -> unit 
```

#### Parameters

end Int32
:   0 for the start Crank, 1 for the end Crank.

crankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The id of a Crank Type element, or invalidElementId if the rebar should have no crank at the specified end.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | the parameter crankTypeId is not a Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
