# Rebar Constraint Get Target Rebar Handle Behavior Method

Source: https://www.revitapidocs.com/2026/d291b8dc-e84a-2d4b-888f-bbbb45691b48.htm

---

| Rebar Constraint Get Target Rebar Handle Behavior Method |
| --- |

Gets the RebarHandleBehavior of the handle of the other Rebar Element to which this RebarConstraint is attached.
 The RebarConstraintType of the RebarConstraint must be 'ToOtherRebar'. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarHandleBehavior GetTargetRebarHandleBehavior()
```

```
Public Function GetTargetRebarHandleBehavior As RebarHandleBehavior
```

```
public:
RebarHandleBehavior GetTargetRebarHandleBehavior()
```

```
member GetTargetRebarHandleBehavior : unit -> RebarHandleBehavior 
```

#### Return Value

[RebarHandleBehavior](Rebar-Handle-Behavior-Enumeration.md) 
Returns the RebarHandleBehavior of the handle of the other Rebar Element to which this RebarConstraint is attached. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | RebarConstraint is no longer valid.  \-or\-  The RebarConstraint is not of RebarConstraintType 'ToOtherRebar'.  \-or\-  Constrained rebar isn't a shape driven rebar element. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarConstraint Class](Rebar-Constraint-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
