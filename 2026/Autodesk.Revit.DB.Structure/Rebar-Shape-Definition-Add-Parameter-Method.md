# Rebar Shape Definition Add Parameter Method

Source: https://www.revitapidocs.com/2026/8e314f3c-3e6c-a3b2-8bd4-68c1fe61b0c4.htm

---

| Rebar Shape Definition Add Parameter Method |
| --- |

Add a parameter to the shape definition. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddParameter(
	ElementId paramId,
	double defaultValue
)
```

```
Public Sub AddParameter ( 
	paramId As ElementId,
	defaultValue As Double
)
```

```
public:
void AddParameter(
	ElementId^ paramId, 
	double defaultValue
)
```

```
member AddParameter : 
        paramId : ElementId * 
        defaultValue : float -> unit 
```

#### Parameters

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The parameter. To obtain the id of a shared parameter,
 call RebarShapeParameters.GetElementIdForExternalDefinition.

defaultValue Double
:   A default value for this parameter in shapes. The default values
 should be chosen carefully, because they are required to be consistent as a set of constraints.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number.  \-or\-  The name of a shared parameter identified by paramId  was already used by another shared parameter of the element. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A shape parameter must be a shared parameter and have value type double.
 A parameter must be added to the definition before it can be used to
 drive the shape in a RebarShapeConstraint object.
 A parameter that does not drive a constraint is legal and will
 simply become an editable parameter on any Rebar that is an instance of this RebarShape. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinition Class](bb1f59be-c95e-a45b-8d2b-8121df179676.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
