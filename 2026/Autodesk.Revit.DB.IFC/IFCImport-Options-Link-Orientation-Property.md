# IFCImport Options Link Orientation Property

Source: https://www.revitapidocs.com/2026/6eeeeb82-c769-ac1e-ea46-e4cb320df9f1.htm

---

| IFCImport Options Link Orientation Property |
| --- |

The orientation of the Linked IFC File in the Host Document. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IFCLinkOrientation LinkOrientation { get; set; }
```

```
Public Property LinkOrientation As IFCLinkOrientation
	Get
	Set
```

```
public:
property IFCLinkOrientation LinkOrientation {
	IFCLinkOrientation get ();
	void set (IFCLinkOrientation value);
}
```

```
member LinkOrientation : IFCLinkOrientation with get, set
```

#### Property Value

[IFCLinkOrientation](IFCLink-Orientation-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCImportOptions Class](IFCImport-Options-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
