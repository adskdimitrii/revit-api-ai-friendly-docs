# IFCImport Options Link Position Property

Source: https://www.revitapidocs.com/2026/e1eee09c-2f35-e140-beb8-8f367fd336f5.htm

---

| IFCImport Options Link Position Property |
| --- |

The position of the Linked IFC File in the Host Document. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IFCLinkPosition LinkPosition { get; set; }
```

```
Public Property LinkPosition As IFCLinkPosition
	Get
	Set
```

```
public:
property IFCLinkPosition LinkPosition {
	IFCLinkPosition get ();
	void set (IFCLinkPosition value);
}
```

```
member LinkPosition : IFCLinkPosition with get, set
```

#### Property Value

[IFCLinkPosition](IFCLink-Position-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCImportOptions Class](IFCImport-Options-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
