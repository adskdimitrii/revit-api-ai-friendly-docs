# Reinforcement Numbering Method Enumeration

Source: https://www.revitapidocs.com/2026/c5278c45-db4d-ec06-4caf-dd395a3bcdee.htm

---

| Reinforcement Numbering Method Enumeration |
| --- |

Defines numbering method settings. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum ReinforcementNumberingMethod
```

```
Public Enumeration ReinforcementNumberingMethod
```

```
public enum class ReinforcementNumberingMethod
```

```
type ReinforcementNumberingMethod
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| AssignUniqueNumberPerSet | 1 | If this value is Assign Unique Numbers Per Set, the following happens: * 1\. The Revit numbering mechanism ( [NumberingSchema](../Autodesk.Revit.DB/Numbering-Schema-Class.md) )  will assign a unique number for each Rebar set which has varying length bars.  Each bar within the varying set will have(share) the same number that was assigned for the entire set. * 2\. Each bar within a set with varying length bars will also be assigned a suffix parameter (REBAR\_NUMBER\_SUFFIX).  This suffix parameter will receive values based on the \[!:RebarVaryingLengthNumberSuffix] property. |
| MatchSetsWithIdenticalBars | 2 | If this value is Match Sets With Identical Bars, the following happens: * 1\. The Revit numbering mechanism ( [NumberingSchema](../Autodesk.Revit.DB/Numbering-Schema-Class.md) )  will assign the same number for Rebar sets with varying length bars if bars at the same index are identical even if these bars are moved. * 2\. Each bar within a set with varying length bars will also be assigned a suffix parameter (REBAR\_NUMBER\_SUFFIX).  This suffix parameter will receive values based on the \[!:RebarVaryingLengthNumberSuffix] property. |
| NumberBarsIndividually | 0 | If this value is Numbers Bars Individually, then the Revit numbering mechanism ( [NumberingSchema](../Autodesk.Revit.DB/Numbering-Schema-Class.md) )  will assign a number to each bar in a rebar set with varying lengths. It will also assign a number to the sets that don't have varying length bars.  The number is assigned based on the Revit numbering logic. (For example if two bars are identical, they will receive the same number).  The numbering mechanism will compare varying bars with other varying or uniform bars within the project. (i.e each bar in a varying set is interpreted as an individual Rebar). *The shape parameters of a Rebar can be accessed via \[!:Autodesk::Revit::DB::Structure::RebarShapeDefinition::getParameters] method.* *The parameters at a specific index in a Rebar set can be accessed via \[!:Autodesk::Revit::DB::Structure::Rebar::getParameterValueAtIndex] method.* |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
