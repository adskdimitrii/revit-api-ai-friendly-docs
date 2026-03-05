# Rebar Number Of Bar Positions Property

Source: https://www.revitapidocs.com/2026/f063cb6e-c159-f0e8-519f-666a797fa53c.htm

---

| Rebar Number Of Bar Positions Property |
| --- |

The number of potential bars in the set. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int NumberOfBarPositions { get; set; }
```

```
Public Property NumberOfBarPositions As Integer
	Get
	Set
```

```
public:
property int NumberOfBarPositions {
	int get ();
	void set (int value);
}
```

```
member NumberOfBarPositions : int with get, set
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: the number of bar positions numberOfBarPositions is less than 1 or more than 1002\. |
| [InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | When setting this property: This rebar element represents a single bar (the layout rule is Single).  \-or\-  When setting this property: The rebar set layout does not permit changing the number of bar positions. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The number of positions is equal to the number of actual bars (the Quantity), plus the number of bars that are excluded.
 The number of bar positions can be set for a rebar set with layout rule FixedNumber or NumberWithSpacing. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
