# Reinforcement Settings Numbering Method Property

Source: https://www.revitapidocs.com/2026/41b7c755-b580-71a4-fa3c-76ed4f4a326a.htm

---

| Reinforcement Settings Numbering Method Property |
| --- |

Identifies the type of the numbering method. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ReinforcementNumberingMethod NumberingMethod { get; set; }
```

```
Public Property NumberingMethod As ReinforcementNumberingMethod
	Get
	Set
```

```
public:
property ReinforcementNumberingMethod NumberingMethod {
	ReinforcementNumberingMethod get ();
	void set (ReinforcementNumberingMethod value);
}
```

```
member NumberingMethod : ReinforcementNumberingMethod with get, set
```

#### Property Value

[ReinforcementNumberingMethod](Reinforcement-Numbering-Method-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property can be used to modify the way that rebar sets with varying length bars are numbered. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ReinforcementSettings Class](Reinforcement-Settings-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
