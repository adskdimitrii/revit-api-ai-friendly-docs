# Rebar Max Spacing Property

Source: https://www.revitapidocs.com/2026/1e7105e5-8d08-26ed-d97d-76754753fded.htm

---

| Rebar Max Spacing Property |
| --- |

Identifies the maximum spacing between rebar in rebar set. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double MaxSpacing { get; set; }
```

```
Public Property MaxSpacing As Double
	Get
	Set
```

```
public:
property double MaxSpacing {
	double get ();
	void set (double value);
}
```

```
member MaxSpacing : float with get, set
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The maxSpacing isn't bigger than 0\.0\. |
| [InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This rebar element represents a single bar (the layout rule is Single).  \-or\-  When setting this property: The rebar set layout does not permit changing the maximum spacing. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The maximum spacing can be set for rebar sets with layout rule MaximumSpacing, MinimumClearSpacing, or NumberWithSpacing. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
