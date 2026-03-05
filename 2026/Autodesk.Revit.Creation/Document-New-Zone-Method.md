# Document New Zone Method

Source: https://www.revitapidocs.com/2026/a0731d97-81ba-be0b-b2df-48f55b06363a.htm

---

| Document New Zone Method |
| --- |

**Note: This API is now obsolete.** 

Creates a new Zone element. 
**Namespace:** [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")]
public Zone NewZone(
	Level level,
	Phase phase
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")>
Public Function NewZone ( 
	level As Level,
	phase As Phase
) As Zone
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")]
Zone^ NewZone(
	Level^ level, 
	Phase^ phase
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")>]
member NewZone : 
        level : Level * 
        phase : Phase -> Zone 
```

#### Parameters

level [Level](577e5d4e-a558-118c-9dea-3b810b061775.htm)
:   The level on which the Zone is to exist.

phase [Phase](ab01f390-a8e8-c21c-b2d0-6dd21056cdec.htm)
:   The associative phase on which the Zone is to exist.

#### Return Value

[Zone](../Autodesk.Revit.DB.Mechanical/Zone-Class.md) 
If successful a new Zone element within the project, otherwise . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the specified parameter Value is . |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the electrical system cannot be created by these input phase and level. |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the level does not exist in the given document. |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the phase does not exist in the given document. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)
