# Rebar Shape Definition Add Formula Parameter Method

Source: https://www.revitapidocs.com/2026/669bcf80-e0b7-ee57-30c0-82fdf4184012.htm

---

| Rebar Shape Definition Add Formula Parameter Method |
| --- |

Add a formula\-driven parameter to the shape definition. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddFormulaParameter(
	ElementId paramId,
	string formula
)
```

```
Public Sub AddFormulaParameter ( 
	paramId As ElementId,
	formula As String
)
```

```
public:
void AddFormulaParameter(
	ElementId^ paramId, 
	String^ formula
)
```

```
member AddFormulaParameter : 
        paramId : ElementId * 
        formula : string -> unit 
```

#### Parameters

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The parameter. To obtain the id of a shared parameter,
 call RebarShapeParameters.GetElementIdForExternalDefinition.

formula String
:   The formula expressed as a string. The string is exactly what a user would
 type into the Family Types dialog, e.g. "Total Length\*3\.14159\*(Bar Diameter/2\)\*(Bar Diameter/2\)"

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not the id of a shared parameter in the current document,  or its unit type is not Reinforcement\_Length, Angle or Number.  \-or\-  The name of a shared parameter identified by paramId  was already used by another shared parameter of the element. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Like AddParameter(), this function introduces a parameter into
 the shape definition, but the parameter's value is driven by a formula.
 Formula parameters cannot be used in constraints to drive the shape.
 The formula is in the same format as in Revit families.
 The formula is allowed to refer to other parameters that are
 already in the definition, plus the builtin parameters REBAR\_INSTANCE\_BAR\_DIAMETER (bar nominal diameter), REBAR\_INSTANCE\_BAR\_MODEL\_DIAMETER (bar model diameter),
 REBAR\_INSTANCE\_BEND\_DIAMETER, REBAR\_SHAPE\_START\_HOOK\_LENGTH, REBAR\_SHAPE\_START\_HOOK\_OFFSET,
 REBAR\_SHAPE\_PARAM\_START\_HOOK\_TAN\_LEN, REBAR\_SHAPE\_PARAM\_END\_HOOK\_TAN\_LEN,
 REBAR\_SHAPE\_END\_HOOK\_LENGTH, REBAR\_SHAPE\_END\_HOOK\_OFFSET, REBAR\_ELEM\_LENGTH,
 REBAR\_ELEM\_TOTAL\_LENGTH, and REBAR\_ELEM\_QUANTITY\_OF\_BARS. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDefinition Class](bb1f59be-c95e-a45b-8d2b-8121df179676.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
