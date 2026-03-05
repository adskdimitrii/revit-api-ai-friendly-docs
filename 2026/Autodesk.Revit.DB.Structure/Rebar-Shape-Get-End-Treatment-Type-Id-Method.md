# Rebar Shape Get End Treatment Type Id Method

Source: https://www.revitapidocs.com/2026/d78defed-af7e-8feb-6e71-2c067fcc3397.htm

---

| Rebar Shape Get End Treatment Type Id Method |
| --- |

**Note: This API is now obsolete.** 

Gets the id of the EndTreatmentType at the specified rebar shape end. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().EndTreatmentTypeIdAtStart or RebarShape.GetTerminationsData().EndTreatmentTypeIdAtEnd instead.")]
public ElementId GetEndTreatmentTypeId(
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().EndTreatmentTypeIdAtStart or RebarShape.GetTerminationsData().EndTreatmentTypeIdAtEnd instead.")>
Public Function GetEndTreatmentTypeId ( 
	end As Integer
) As ElementId
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().EndTreatmentTypeIdAtStart or RebarShape.GetTerminationsData().EndTreatmentTypeIdAtEnd instead.")]
ElementId^ GetEndTreatmentTypeId(
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().EndTreatmentTypeIdAtStart or RebarShape.GetTerminationsData().EndTreatmentTypeIdAtEnd instead.")>]
member GetEndTreatmentTypeId : 
        end : int -> ElementId 
```

#### Parameters

end Int32
:   0 for the start end treatment, 1 for the end end treatment.

#### Return Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
Returns the id of an EndTreatmentType, or invalidElementId if the rebar shape has no end treatment at the specified end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | end not a valid shape end |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
