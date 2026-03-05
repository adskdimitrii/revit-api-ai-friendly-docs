# Rebar Set End Treatment Type Id Method

Source: https://www.revitapidocs.com/2026/ceb68db2-2053-5911-3318-da05ec742dac.htm

---

| Rebar Set End Treatment Type Id Method |
| --- |

Sets the id of the EndTreatmentType to be applied to the rebar.
 This can be done if and only if the end of the bar on which the end treatment is applied has no RebarCoupler on it, otherwise will throw an exception. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetEndTreatmentTypeId(
	int end,
	ElementId endTreatmentTypeId
)
```

```
Public Sub SetEndTreatmentTypeId ( 
	end As Integer,
	endTreatmentTypeId As ElementId
)
```

```
public:
void SetEndTreatmentTypeId(
	int end, 
	ElementId^ endTreatmentTypeId
)
```

```
member SetEndTreatmentTypeId : 
        end : int * 
        endTreatmentTypeId : ElementId -> unit 
```

#### Parameters

end Int32
:   0 for the start end treatment, 1 for the end end treatment.

endTreatmentTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The id of a EndTreatmentType element, or invalidElementId if
 the rebar should have no end treatment at the specified end.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | the parameter endTreatmentTypeId is not an EndTreatmentType element. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | the Rebar end end has a RebarCoupler on it. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
