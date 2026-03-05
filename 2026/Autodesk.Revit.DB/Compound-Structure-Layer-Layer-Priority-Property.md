# Compound Structure Layer Layer Priority Property

Source: https://www.revitapidocs.com/2026/3697dca7-3b28-1757-1191-6b60ad556304.htm

---

| Compound Structure Layer Layer Priority Property |
| --- |

The priority of the layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int LayerPriority { get; set; }
```

```
Public Property LayerPriority As Integer
	Get
	Set
```

```
public:
property int LayerPriority {
	int get ();
	void set (int value);
}
```

```
member LayerPriority : int with get, set
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The effective priority value should be between 1\-5\. Membrane layers should not have a priority, the value should be 999\.
 You should set the layer priority if you want a customized priority value rather than the default one by function.
 In shell, a non\-membrane layer which is closer to the core should not have a lower priority. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructureLayer Class](Compound-Structure-Layer-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
