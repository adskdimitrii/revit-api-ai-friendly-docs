# Rebar Get End Treatment Type Id Method

Source: https://www.revitapidocs.com/2026/3521d0c8-5746-6dde-4839-3e9a14dbd93e.htm

---

| Rebar Get End Treatment Type Id Method |
| --- |

Get the id of the EndTreatmentType that is applied to the rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GetEndTreatmentTypeId(
	int end
)
```

```
Public Function GetEndTreatmentTypeId ( 
	end As Integer
) As ElementId
```

```
public:
ElementId^ GetEndTreatmentTypeId(
	int end
)
```

```
member GetEndTreatmentTypeId : 
        end : int -> ElementId 
```

#### Parameters

end Int32
:   0 for the start end treatment, 1 for the end end treatment.

#### Return Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
The id of a EndTreatmentType, or invalidElementId if the rebar has
 no end treatment at the specified end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
