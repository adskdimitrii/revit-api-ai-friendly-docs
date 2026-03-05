# Cable Size Number Of Ground Conductors Property

Source: https://www.revitapidocs.com/2026/ff6836f3-6f4f-ec8f-7d5e-d2da45d1fa1f.htm

---

| Cable Size Number Of Ground Conductors Property |
| --- |

The number of Ground Conductors. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int NumberOfGroundConductors { get; set; }
```

```
Public Property NumberOfGroundConductors As Integer
	Get
	Set
```

```
public:
property int NumberOfGroundConductors {
	int get ();
	void set (int value);
}
```

```
member NumberOfGroundConductors : int with get, set
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for numberOfGroundConductors is negative. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CableSize Class](Cable-Size-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
