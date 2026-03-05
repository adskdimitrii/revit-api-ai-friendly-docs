# Reinforcement Settings Number Varying Length Rebars Individually Property

Source: https://www.revitapidocs.com/2026/7b74062d-8c65-4145-1d8c-23302ebc5b61.htm

---

| Reinforcement Settings Number Varying Length Rebars Individually Property |
| --- |

**Note: This API is now obsolete.** 

Use this option to modify the way varying length bars are numbered (individually or as a whole). 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use the 'NumberingMethod' property instead.")]
public bool NumberVaryingLengthRebarsIndividually { get; set; }
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use the 'NumberingMethod' property instead.")>
Public Property NumberVaryingLengthRebarsIndividually As Boolean
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use the 'NumberingMethod' property instead.")]
property bool NumberVaryingLengthRebarsIndividually {
	bool get ();
	void set (bool value);
}
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use the 'NumberingMethod' property instead.")>]
member NumberVaryingLengthRebarsIndividually : bool with get, set
```

#### Property Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If this property is true it will correspond to \[!:Autodesk::Revit::DB::ReinforcementNumberingMethod::NumberBarsIndividually] .
 If this property is false, it may correspond to \[!:Autodesk::Revit::DB::ReinforcementNumberingMethod::AssignUniqueNumberPerSet] or \[!:Autodesk::Revit::DB::ReinforcementNumberingMethod::MatchSetsWithIdenticalBars] .
 If you set it to true, it will correspond to \[!:Autodesk::Revit::DB::ReinforcementNumberingMethod::NumberBarsIndividually] .
 If you set it to false, it will correspond to \[!:Autodesk::Revit::DB::ReinforcementNumberingMethod::AssignUniqueNumberPerSet] . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ReinforcementSettings Class](Reinforcement-Settings-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
