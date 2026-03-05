# View Anchor Enumeration

Source: https://www.revitapidocs.com/2026/8620fc3d-ce84-40d0-dc89-c8c042acbb81.htm

---

| View Anchor Enumeration |
| --- |

An enumerated type listing options for the anchor point used by the placed view. The anchor point determines how the view position is updated if assigned to a saved position or swapped to another view. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum ViewAnchor
```

```
Public Enumeration ViewAnchor
```

```
public enum class ViewAnchor
```

```
type ViewAnchor
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| BottomLeft | 5 | Available for crop\-region enabled views and aligns the view using the bottom left of the crop region boundary as the reference. |
| BottomRight | 4 | Available for crop\-region enabled views and aligns the view using the bottom right of the crop region boundary as the reference. |
| Center | 1 | Available for crop\-region enabled views and aligns the view using the center of the crop region boundary as the reference. |
| TopLeft | 2 | Available for crop\-region enabled views and aligns the view using the top left of the crop region boundary as the reference. |
| TopRight | 3 | Available for crop\-region enabled views and aligns the view using the top right of the crop region boundary as the reference. |
| ViewOrigin | 0 | Available for all views and aligns the view using the origin of the view as the reference. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
